<template>
  <div class="sidebar"
       :style="sidebarStyle">
      <div class="sidebar-wrapper">
        <div class="introduction">
          <h3><b>Good Morning,</b></h3>
          <h5>{{title}}</h5>
          <img src="./../../assets/images/cat_glasses.png" width="50%">
        </div>
      </div>
  </div>
</template>
<script>
  import SidebarLink from './SidebarLink.vue'

  export default {
    components: {
      SidebarLink
    },
    props: {
      title: {
        type: String,
        default: 'Dr. Heinz Doofenshmirtz'
      },
      sidebarLinks: {
        type: Array,
        default: () => []
      },
      autoClose: {
        type: Boolean,
        default: true
      }
    },
    provide () {
      return {
        autoClose: this.autoClose
      }
    },
    computed: {
      sidebarStyle () {
        return {}
      }
    }
  }

</script>
<style>
  .sidebar .sidebar-wrapper {
    display: flex;
    flex-direction: column;
    text-align: center;
  }
 .sidebar .nav-main__links {
   flex: 1;
 }
 .sidebar .sidebar-wrapper .logo .logo__container {
   padding-left: 10px;
 }
 img {
  border-radius: 50%;
}
</style>
