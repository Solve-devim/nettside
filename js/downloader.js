function createDownloadButton() {
    const button = document.createElement("button");
    button.innerText = "Last Ned";

    button.classList.add("btn", "btn-primary");
    
    button.addEventListener("click", () => {
        const link = document.createElement("a");
        link.href = "assets/Slot-Maskin.zip";  
        link.download = "Slot Maskin.zip"; 
        link.click();
    });
    
    document.getElementById("button-container").appendChild(button);
}

createDownloadButton();
