function scanningUrl(info) {

    link = info.linkUrl
    alert(link)

}

chrome.contextMenus.create({
    title: "Scan with HunterPhisher",
    contexts: ["link", "image", "selection"],
    onclick: scanningUrl
});