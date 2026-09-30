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
    // this allows cheating and it should be access restricted
    #[Route('/sinje/cooldown', name: 'app_sinje_cooldown', methods: ['GET'])]
    public function cooldownsinje(
        SinjeCooldownRepository $sinjeCooldownRepository
    ): JsonResponse {
        $cooldown = $sinjeCooldownRepository->findAll()[0]->getCooldown();

        return $this->json([
            $cooldown
        ]);
    }

    #[Route('/sinje/cop/{id_user}', name: 'app_sinje_cop', methods: ['GET'])]
    public function copsinje(
        int $id_user,
        EntityManagerInterface $entityManager,
        SinjeRepository $sinjeRepository,
        SinjeCooldownRepository $sinjeCooldownRepository,
        Request $request
    ): JsonResponse {
        // check cooldown to see if it's up
        $cooldown = $sinjeCooldownRepository->findAll()[0];
        if ($cooldown->getCooldown() < time() ){
           
            $newcd = time() + rand(6 * 3600, 18 * 3600);
            $newuser = $id_user;
            $oldsinje = $sinjeRepository->findOneBy([], ['id' => 'DESC']);

            //previous owner and how long the cooldown has been available before activation
            //not counting the static cooldown as detention time because it's random
            $olduser = $oldsinje->getUserid();
            $possession = time() - $cooldown->getCooldown();

            //set new cooldown
            $cooldown->setCooldown($newcd);

            //create new sinje
            $newsinje = new Sinje();
            $newsinje->setUserId($newuser);
            $newsinje->setLastUser($olduser);
            $newsinje->setPossession($possession);

            $entityManager->persist($cooldown);
            $entityManager->persist($newsinje);
            $entityManager->flush();

        return $this->json([
            "sinje acquired"
        ]);
        } else {
                    return $this->json([
            "not available"
        ]);
        }

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

