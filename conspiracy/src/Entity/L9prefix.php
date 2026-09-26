<?php

namespace App\Entity;

use App\Repository\L9prefixRepository;
use Doctrine\ORM\Mapping as ORM;

#[ORM\Entity(repositoryClass: L9prefixRepository::class)]
class L9prefix
{
    #[ORM\Id]
    #[ORM\GeneratedValue]
    #[ORM\Column]
    private ?int $id = null;

    #[ORM\Column(length: 255)]
    private ?string $prefix = null;

    public function getId(): ?int
    {
        return $this->id;
    }

    public function getPrefix(): ?string
    {
        return $this->prefix;
    }

    public function setPrefix(string $prefix): static
    {
        $this->prefix = $prefix;

        return $this;
    }
}
