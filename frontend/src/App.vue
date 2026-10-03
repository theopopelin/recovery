<script setup>
import SinjeScoreboard from './components/SinjeScoreboard.vue'
</script>

<template>
    <div class="app">

        <div class="background">

            <div class="scanlines"></div>

            <div class="noise"></div>
            <div class="noise noise-moving"></div>

            <div class="background-text play">
                PLAY SINJE
            </div>

            <div class="background-text time">
                --:--
            </div>

            <div class="background-text record-speed">
                SLP 0:17:44
            </div>

        </div>

        <SinjeScoreboard />

    </div>
</template>