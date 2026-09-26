<?php

namespace App\Entity;

use App\Repository\SinjeRepository;
use Doctrine\DBAL\Types\Types;
use Doctrine\ORM\Mapping as ORM;

#[ORM\Entity(repositoryClass: SinjeRepository::class)]
class Sinje
{
    #[ORM\Id]
    #[ORM\GeneratedValue]
    #[ORM\Column]
    private ?int $id = null;

    #[ORM\Column(type: Types::BIGINT)]
    private ?string $userid = null;

    #[ORM\Column(type: Types::BIGINT)]
    private ?string $lastuser = null;

    #[ORM\Column(type: Types::BIGINT)]
    private ?string $possession = null;

    public function getId(): ?int
    {
        return $this->id;
    }

    public function getUserid(): ?string
    {
        return $this->userid;
    }

    public function setUserid(string $userid): static
    {
        $this->userid = $userid;

        return $this;
    }

    public function getLastuser(): ?string
    {
        return $this->lastuser;
    }

    public function setLastuser(string $lastuser): static
    {
        $this->lastuser = $lastuser;

        return $this;
    }

    public function getPossession(): ?string
    {
        return $this->possession;
    }

    public function setPossession(string $possession): static
    {
        $this->possession = $possession;

        return $this;
    }
}
