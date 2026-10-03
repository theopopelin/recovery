export function formatPossession(seconds) {
    const days = Math.floor(seconds / 86400)
    seconds %= 86400

    const hours = Math.floor(seconds / 3600)
    seconds %= 3600

    const minutes = Math.floor(seconds / 60)

    if (days > 0) {
        return `${days}j ${hours}h`
    }

    if (hours > 0) {
        return `${hours}h ${minutes}min`
    }

    return `${minutes}min`
}