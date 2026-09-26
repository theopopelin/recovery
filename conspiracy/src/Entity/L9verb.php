<?php

namespace App\Entity;

use App\Repository\L9verbRepository;
use Doctrine\ORM\Mapping as ORM;

#[ORM\Entity(repositoryClass: L9verbRepository::class)]
class L9verb
{
    #[ORM\Id]
    #[ORM\GeneratedValue]
    #[ORM\Column]
    private ?int $id = null;

    #[ORM\Column(length: 255)]
    private ?string $verb = null;

    public function getId(): ?int
    {
        return $this->id;
    }

    public function getVerb(): ?string
    {
        return $this->verb;
    }

    public function setVerb(string $verb): static
    {
        $this->verb = $verb;

        return $this;
    }
}
