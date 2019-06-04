export const get = async(query) => {
    const res = fetch(query)
        .then(handleServerResponse)
    return res
}

export const uploadImage = async(imageFile, title, description, extra) => {
    console.log(imageFile, "files")

    let form = new FormData()
    form.append("file", imageFile)
    form.append("title", title)
    form.append("description", description)
    form.append("extra", extra)

    const res = fetch("/image/upload", {
        method: "POST",
        body: form
    }).then(handleServerResponse)
        .catch(res => [])

    return res
}

const handleServerResponse = async(response) => {
    try {
        let json_response = await response.json()
        if (response.ok) {
            return json_response
        } else {
            alert(json_response.message)
            return []
        }

    } catch(e) {
        alert("Operation failed")
        return []
    }

}
