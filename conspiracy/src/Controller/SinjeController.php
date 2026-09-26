<?php

namespace App\Controller;

use App\Entity\Sinje;
use App\Repository\SinjeRepository;
use App\Repository\SinjeCooldownRepository;
use Doctrine\ORM\EntityManagerInterface;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\Routing\Attribute\Route;

class SinjeController extends AbstractController
{
    #[Route('/sinje/cooldown', name: 'app_sinje_cooldown', methods: ['GET'])]
    public function cooldownsinje(
        SinjeCooldownRepository $sinjeCooldownRepository
    ): JsonResponse {
        $cooldown = $sinjeCooldownRepository->findAll()[0]->getCooldown();

        return $this->json([
            $cooldown
        ]);
    }

    #[Route('/sinje/cop', name: 'app_sinje_cop', methods: ['GET'])]
    public function copsinje(
        EntityManagerInterface $entityManager,
        SinjeCooldownRepository $sinjeCooldownRepository,
        Request $request
    ): JsonResponse {
        $newcd = $request->query->get('cd');
        $newuser = $request->query->get('newuser');
        $olduser = $request->query->get('olduser');
        $possession = $request->query->get('possession');

        $cooldown = $sinjeCooldownRepository->findAll()[0];
        $cooldown->setCooldown($newcd);

        $newsinje = new Sinje();
        $newsinje->setUserId($newuser);
        $newsinje->setLastUser($olduser);
        $newsinje->setPossession($possession);

        $entityManager->persist($newsinje);
        $entityManager->flush();

        return $this->json([
            'message' => 'Welcome to your new controller!',
            'path' => 'src/Controller/SinjeController.php',
        ]);
    }

    #[Route('/sinje/combien/{id_user}', name: 'app_sinje_combien', methods: ['GET'])]
    public function combiensinje(
        int $id_user,
        SinjeRepository $sinjeRepository
    ): JsonResponse {
        $sinjes = $sinjeRepository->findBy([
            'userid' => $id_user
        ]);

        $nombresinjes = count($sinjes);

        return $this->json([
            $nombresinjes
        ]);
    }
}

