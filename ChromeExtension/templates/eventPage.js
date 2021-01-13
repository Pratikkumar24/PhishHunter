function scanningUrl(info) {

    link = info.linkUrl
    if (link && !info.selectionText) {
        console.log("\nThe Link: " + link);
    } else if (info.selectionText && !link) {
        console.log("\nThe Link: " + link);

    }
}

chrome.contextMenus.create({
    title: "Scan with HunterPhisher",
    contexts: ["link", "image", "selection"],
    onclick: scanningUrl
});