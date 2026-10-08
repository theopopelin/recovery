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

        return new JsonResponse([
            'success' => true,
            'message' => 'Ticket sent'
        ], 201);
    }
}
