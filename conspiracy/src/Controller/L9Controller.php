<?php

namespace App\Controller;

use App\Repository\L9prefixRepository;
use App\Repository\L9verbRepository;
use App\Repository\L9lowRepository;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

class L9Controller
{
    #[Route('/l9/prefix', methods: ['GET'])]
    public function prefix(L9prefixRepository $repository): JsonResponse
    {
        $words = $repository->findAll();

        if (empty($words)) {
            return new JsonResponse([
                'error' => 'Empty'
            ], 404);
        }

        $prefix = $words[array_rand($words)];

        return new JsonResponse($prefix->getPrefix());
    }

    #[Route('/l9/verb', methods: ['GET'])]
    public function verb(L9verbRepository $repository): JsonResponse
    {
        $words = $repository->findAll();

        if (empty($words)) {
            return new JsonResponse([
                'error' => 'Empty'
            ], 404);
        }

        $verb = $words[array_rand($words)];

        return new JsonResponse($verb->getVerb());
    }

    #[Route('/l9/low', methods: ['GET'])]
    public function low(L9lowRepository $repository): JsonResponse
    {
        $words = $repository->findAll();

        if (empty($words)) {
            return new JsonResponse([
                'error' => 'Empty'
            ], 404);
        }

        $low = $words[array_rand($words)];

        return new JsonResponse($low->getLow());
    }

    #[Route('/l9/random', methods: ['GET'])]
    public function random(L9prefixRepository $prefixrepository, L9lowRepository $lowrepository, L9verbRepository $verbrepository): JsonResponse
    {
        $allprefix = $prefixrepository->findAll();
        $allverb = $verbrepository->findAll();
        $alllow = $lowrepository->findAll();

         if (empty($allprefix) || empty($allverb) || empty($alllow)) {
            return new JsonResponse([
                'error' => 'Empty'
            ], 404);
        }

        $prefix = $allprefix[array_rand($allprefix)];
        $verb = $allverb[array_rand($allverb)];
        $low = $alllow[array_rand($alllow)];

        return new JsonResponse([
            'prefix' => $prefix->getPrefix(),
            'verb' => $verb->getVerb(),
            'low' => $low->getLow()
        ]);
    }

}