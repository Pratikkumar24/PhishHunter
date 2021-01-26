async function scanningUrl(info) {


    const formData = new FormData();

    if (info.selectionText) {
        link = info.selectionText
    } else if (info.linkUrl) {
        link = info.linkUrl
    } else {
        link = "X";
    }


    formData.append('url', link);

    const response = await fetch('http://127.0.0.1:5000/', {
        method: 'POST',
        headers: {
            contentType: 'application/json'
        },
        body: formData,

    })


    const res = await response.json()
    result = res['response']
        // console.log(result)
        // alert(result)

}

chrome.contextMenus.create({
    title: "Scan with PhishHunter",
    contexts: ["link", "image", "selection"],
    onclick: scanningUrl
});