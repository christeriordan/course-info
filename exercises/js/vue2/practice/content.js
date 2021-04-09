
let box = {
    props: ["nr", "title","color"],
    template:`<div class="box" v-bind:style="{color: color}" v-on:click="$emit(´hello')>HW! #{{nr}} {{title}}</div>`
}