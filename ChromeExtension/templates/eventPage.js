async function scanningUrl(info) {
    const formData = new FormData();
    link = info.url
    console.log("the link: " + link);
    formData.append('url', link);

    const response = await fetch('http://127.0.0.1:5000/', {
        method: 'POST',
        headers: {
            contentType: 'application/json'
        },
        body: formData,

    })
    const res = await response.json()
        // console.log(res['response'])
        // alert(res['response'])
    result = res['response']

    alert("Here is the result =>" + result)
        // swal('PhishHunter', 'Your result', 'success')
}

chrome.contextMenus.create({
    title: "Scan with HunterPhisher",
    contexts: ["link", "image", "selection"],
    onclick: scanningUrl
});