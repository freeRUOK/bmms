let menuComponent = {
  template: `<div id="component1" @load="loadDoc"><div v-html="doc"></div></div>`, 
  data () {
    return {doc: `<h1>正在加载。。。。。</h1>`}
  }, 
  computed: {loadDoc () {
    axios.get("https://github.com/")
      .then((res) => (this.doc = res.data))
      .catch((err) => (this.doc = `<h1>应用程序不可用</h1>`))
  }}
}

let showComponent = {
  template: ``
}

window.addEventListener("load", function () {
  const vueApp = Vue.createApp({"components": {"menu-component": menuComponent, "show-component": showComponent}});
  vueApp.mount("#app");
});
