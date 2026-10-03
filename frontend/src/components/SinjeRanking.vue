<script setup>
defineProps({
    users: Array,
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
    <section class="ranking">

        <h2>Classement</h2>

        <article
            v-for="(user, index) in users"
            :key="user.user_id"
            class="ranking-row"
        >
            <span class="position">
                #{{ index + 1 }}
            </span>

            <img
                v-if="user.avatar"
                :src="user.avatar"
                :alt="user.global_name || user.username"
                class="small-avatar"
            />

            <div v-else class="small-avatar placeholder">
                ?
            </div>

            <div class="identity">
                <strong>
                    {{ user.global_name || user.username }}
                </strong>

                <span>
                    @{{ user.username }}
                </span>
            </div>

            <div class="stats">
                <strong>{{ user.count }}</strong>
                <span>Sinjes</span>
            </div>

            <div class="stats">
                <strong>
                    {{ getPercentage(user.count, total) }}%
                </strong>
                <span>du total</span>
            </div>

            <div class="stats">
                <strong>
                    {{ formatPossession(user.possession) }}
                </strong>
                <span>possession</span>
            </div>
        </article>

    </section>
</template>
<style src="../assets/ranking.css"></style>