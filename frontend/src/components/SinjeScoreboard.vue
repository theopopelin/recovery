<script setup>
import { computed, onMounted, ref } from 'vue'
import SinjeTopUser from './SinjeTopUser.vue'
import SinjeDistribution from './SinjeDistribution.vue'
import SinjeRanking from './SinjeRanking.vue'

import sinjeLoading from '../assets/sinje-loading.gif'

const scoreboard = ref(null)
const loading = ref(true)
const error = ref(null)

const rankedUsers = computed(() => {
    if (!scoreboard.value) {
        return []
    }

    return [...scoreboard.value.users].sort(
        (a, b) => b.count - a.count
    )
})

async function fetchScoreboard() {
    try {
        const response = await fetch(
            `${import.meta.env.VITE_API_URL}/sinje/scoreboard`
        )

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`)
        }

        scoreboard.value = await response.json()
    } catch (err) {
        error.value = err.message
    } finally {
        loading.value = false
    }
}

onMounted(fetchScoreboard)
</script>

<template>
    <main class="scoreboard">

            <div v-if="loading" class="state loading-state">
                <img
                    :src="sinjeLoading"
                    alt="Chargement..."
                />

                <p>Just a second...</p>
            </div>

        <div v-else-if="error" class="state error">
            Impossible de récupérer le scoreboard.
            <br />
            <small>{{ error }}</small>
        </div>

        <template v-else-if="scoreboard">

            <section class="top-section">

                <SinjeTopUser
                    :user="rankedUsers[0]"
                    :total="scoreboard.total"
                />

                <SinjeDistribution
                    :users="rankedUsers"
                    :total="scoreboard.total"
                />

            </section>

            <SinjeRanking
                :users="rankedUsers"
                :total="scoreboard.total"
            />

        </template>

    </main>
</template>

<style src="../assets/scoreboard.css"></style>