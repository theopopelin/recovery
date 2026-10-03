<script setup>
defineProps({
    user: Object,
    total: Number
})

import { formatPossession } from '../utils/formatPossession'

function getPercentage(count, total) {
    if (!total) {
        return 0
    }

    return ((count / total) * 100).toFixed(1)
}

</script>

<template>
    <article v-if="user" class="rank-one">

        <div class="rank-one-label">
            RANK ONE NUMERO UNO<br>
            THE SINJE GOAT 😎

        </div>

        <img
            v-if="user.avatar"
            :src="user.avatar"
            :alt="user.global_name || user.username"
            class="rank-one-avatar"
        />

        <div v-else class="rank-one-avatar placeholder">
            ?
        </div>

        <h2>
            {{ user.global_name || user.username }}
        </h2>

        <p class="username">
            @{{ user.username }}
        </p>

        <div class="rank-one-stats">
            <strong>{{ user.count }}</strong>
            <span>Sinjes</span>
        </div>

        <div class="rank-one-percentage">
            {{ getPercentage(user.count, total) }} % du total
        </div>

        <div class="rank-one-possession">
            {{ formatPossession(user.possession) }}
            de possession
        </div>

    </article>
</template>
<style src="../assets/top-user.css"></style>