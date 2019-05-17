export const get = async(query) => {
    const res = await fetch(query)
    if(res.status !== 200) {
        return [];
    }
    return res.json()
}
