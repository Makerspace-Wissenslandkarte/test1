// Define a new component called todo-item
Vue.component("tags", {
  template:
    ' <ul class="menu-list"><li><button class="button is-3 is-info is-centered m-1">{{tag}}</button></li></ul>',
});

var vueprofile = new Vue({
  el: "#tags",
  data: {
    showNav: false,
    tag: "Holz",
  },
});
