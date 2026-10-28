<?php

namespace App\Controller;

use App\Entity\Ticket;
use App\Repository\TicketRepository;
use Doctrine\ORM\EntityManagerInterface;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\Routing\Attribute\Route;

class TicketController
{
    #[Route('/ticket/create', name: 'ticket_create', methods: ['POST', 'OPTIONS'])]
    public function createTicket(
        Request $request,
        TicketRepository $ticketRepository,
        EntityManagerInterface $entityManager
    ): JsonResponse {
        if ($request->isMethod('OPTIONS')) {
            return new JsonResponse(null, 204);
        }
        $data = json_decode($request->getContent(), true);

        $name = $data['name'] ?? null;
        $email = $data['email'] ?? null;
        $message = $data['message'] ?? null;

        // check fields
        if (empty($name) || empty($email) || empty($message)) {
            return new JsonResponse([
                'success' => false,
                'message' => 'all fields are required.'
            ], 400);
        }

        // check for dupes
        $existingTicket = $ticketRepository->findOneBy([
            'name' => $name,
            'email' => $email,
            'message' => $message
        ]);

        if ($existingTicket !== null) {
            // Reset notification status
            $existingTicket->setNotifiedAt(null);

            $entityManager->flush();

            return new JsonResponse([
                'success' => true,
                'message' => 'Ticket sent'
            ], 200);
        }

        // create ticket
        $ticket = new Ticket();

        $ticket->setName($name);
        $ticket->setEmail($email);
        $ticket->setMessage($message);
        $ticket->setCreatedAt(new \DateTimeImmutable());

        $entityManager->persist($ticket);
        $entityManager->flush();

        // Notify Discord after saving the ticket
        $this->sendDiscordNotification($ticket);

        return new JsonResponse([
            'success' => true,
            'message' => 'Ticket sent'
        ], 201);
    }

    private function sendDiscordNotification(Ticket $ticket): void
    {
        $webhookUrl = getenv('DISCORD_WEBHOOK_URL');

        if (!$webhookUrl) {
            error_log('Discord webhook URL is not configured.');
            return;
        }

        $createdAt = $ticket->getCreatedAt();

        $payload = [
            'embeds' => [
                [
                    'title' => '📩 Nouveau ticket Recovery',
                    'color' => 5793266,
                    'fields' => [
                        [
                            'name' => 'Nom',
                            'value' => substr($ticket->getName() ?? '', 0, 256),
                            'inline' => true,
                        ],
                        [
                            'name' => 'E-mail',
                            'value' => substr($ticket->getEmail() ?? '', 0, 256),
                            'inline' => true,
                        ],
                        [
                            'name' => 'Message',
                            'value' => substr($ticket->getMessage() ?? '', 0, 1024),
                            'inline' => false,
                        ],
                    ],
                    'footer' => [
                        'text' => 'Recovery • Ticket #' . $ticket->getId(),
                    ],
                    'timestamp' => $createdAt?->format(
                        \DateTimeInterface::ATOM
                    ),
                ],
            ],
            'allowed_mentions' => [
                'parse' => [],
            ],
        ];

        $context = stream_context_create([
            'http' => [
                'method' => 'POST',
                'header' => implode("\r\n", [
                    'Content-Type: application/json',
                    'Accept: application/json',
                ]),
                'content' => json_encode(
                    $payload,
                    JSON_UNESCAPED_UNICODE | JSON_INVALID_UTF8_SUBSTITUTE
                ),
                'timeout' => 3,
                'ignore_errors' => true,
            ],
        ]);

        try {
            $response = @file_get_contents(
                $webhookUrl,
                false,
                $context
            );

            $statusLine = $http_response_header[0] ?? '';
            preg_match('/\s(\d{3})\s/', $statusLine, $matches);
            $statusCode = (int) ($matches[1] ?? 0);

            if ($response === false || $statusCode < 200 || $statusCode >= 300) {
                error_log(
                    sprintf(
                        'Discord webhook failed. HTTP status: %d',
                        $statusCode
                    )
                );
            }
        } catch (\Throwable $exception) {
            error_log('Discord webhook error: ' . $exception->getMessage());
        }
    }
}
