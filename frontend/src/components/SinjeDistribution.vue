<script setup>
import { computed } from 'vue'

const props = defineProps({
    users: {
        type: Array,
        required: true
    },
    total: {
        type: Number,
        required: true
    }
})

function getPercentage(count) {
    if (!props.total) {
        return 0
    }

    return ((count / props.total) * 100).toFixed(1)
}

const pieData = computed(() => {
    const topFive = props.users.slice(0, 5)

    const topFiveCount = topFive.reduce(
        (total, user) => total + user.count,
        0
    )

    const othersCount = props.total - topFiveCount

    const data = topFive.map(user => ({
        label: user.global_name || user.username,
        count: user.count,
        percentage: getPercentage(user.count)
    }))

    if (othersCount > 0) {
        data.push({
            label: 'Autres',
            count: othersCount,
            percentage: getPercentage(othersCount)
        })
    }

    return data
})

const pieStyle = computed(() => {
    let currentPercentage = 0

    const segments = pieData.value.map((user, index) => {
        const start = currentPercentage
        const end = currentPercentage + Number(user.percentage)

        currentPercentage = end

        return `var(--pie-color-${index + 1}) ${start}% ${end}%`
    })

    return {
        background: `conic-gradient(${segments.join(', ')})`
    }
})
</script>

<template>
    <article class="distribution">

        <div class="distribution-header">
            <h2>Répartition</h2>

            <span>
                {{ total }} Sinjes
            </span>
        </div>

        <div class="pie-container">

            <div
                class="pie"
                :style="pieStyle"
            >
                <div class="pie-center">
                    <strong>
                        {{ total }}
                    </strong>

                    <span>
                        Sinjes
                    </span>
                </div>
            </div>

            <div class="pie-legend">

                <div
                    v-for="(user, index) in pieData"
                    :key="user.label"
                    class="legend-item"
                >
                    <span
                        class="legend-color"
                        :style="{
                            backgroundColor:
                                `var(--pie-color-${index + 1})`
                        }"
                    ></span>

                    <span class="legend-name">
                        {{ user.label }}
                    </span>

                    <strong>
                        {{ user.percentage }}%
                    </strong>
                </div>

            </div>

        </div>

            <div class="game-info">
                    <p>
                        Envie de participer ?
                    </p>

                    <span>
                        Apes, together, strong. Rejoins un serveur Discord avec le Bot K2000 ou invite le sur ton serveur et tente de récupérer le prochain Sinje.
                    </span>
                </div>

                <a
                    href="https://discord.com/api/oauth2/authorize?client_id=895281877571764264&permissions=8&scope=bot"
                    target="_blank"
                    rel="noopener noreferrer"
                    class="discord-invite"
                >
                    Inviter K2000 sur mon serveur
                </a>

    </article>
</template>
<style src="../assets/distribution.css"></style>