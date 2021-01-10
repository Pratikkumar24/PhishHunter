function scanningUrl(info) {

    if (info.linkUrl && !info.selectionText) {
        chrome.tabs.create({ url: info.linkUrl })
    } else if (info.selectionText && !info.linkUrl) {
        chrome.tabs.create({ url: info.selectionText })

    }
}

chrome.contextMenus.create({
    title: "Scan with HunterPhisher",
    contexts: ["link", "selection"],
    onclick: scanningUrl
});