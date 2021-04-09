
let app = Vue.createApp({
    data: function(){
        return {count: "1"}
    },
    methods: {
        clicked: function(){
            this.$emit('hello')
        }
    }
})


app.component("my-box", box)
app.mount("#app")