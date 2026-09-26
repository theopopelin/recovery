<?php

namespace App\Entity;

use App\Repository\L9lowRepository;
use Doctrine\ORM\Mapping as ORM;

#[ORM\Entity(repositoryClass: L9lowRepository::class)]
class L9low
{
    #[ORM\Id]
    #[ORM\GeneratedValue]
    #[ORM\Column]
    private ?int $id = null;

    #[ORM\Column(length: 255)]
    private ?string $low = null;

    public function getId(): ?int
    {
        return $this->id;
    }

    public function getLow(): ?string
    {
        return $this->low;
    }

    public function setLow(string $low): static
    {
        $this->low = $low;

        return $this;
    }
}
