function reveal(id, event) {
    hide()
    let card = document.getElementById(id)
    card.style.display = "flex"
    let x = event.clientX
    let y = event.clientY
    if (screen.width < 900) {
        card.style.top = y - 20 + 280 + 'px'
    }
    else {
        card.style.top = y - 10 + 'px'
    }
    card.style.left = x - 10 + 'px'
}

function hide() {
    let Event_detail_card = document.getElementsByClassName('Event_detail_card')
    for (let index = 0; index < Event_detail_card.length; index++) {
        const element = Event_detail_card[index];
        element.style.display = "none"
    }
}