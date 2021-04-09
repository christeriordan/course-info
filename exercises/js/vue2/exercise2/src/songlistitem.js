
let songlistItem = {
    props: ['song'],
    template: /*html*/ `<li>
        <img 
            src="images/delete.png" 
            alt="delete" 
            class="delete" 
            v-on:click="$emit('delete')">
        <div>{{ song.name }}</div>
        <div>{{ song.band }}</div>
    </li>`
}
/*
<ul id="playlist">
<li v-for="(song, index) in playlist">
    <img src="images/delete.png" alt="delete" class="icon" v-on:click="remove(index)">
    <img src="images/play.png" alt="play" class="icon" v-on:click="play(index)">
    <span class="inlist">{{ song.name }}</span>
    <span class="inlist band">{{ song.band }}</span>
    <span class="inlist">played {{ song.played ? song.played : "0" }} times</span>
</li>
</ul>
*/