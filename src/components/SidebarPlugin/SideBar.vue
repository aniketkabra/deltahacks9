<template>
  <div class="sidebar"
       :style="sidebarStyle">
      <div class="sidebar-wrapper">
        <div class="introduction">
          <h5><b>Good Morning,</b></h5>
          <p>{{title}}</p>
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
  }
 .sidebar .nav-main__links {
   flex: 1;
 }
 .sidebar .sidebar-wrapper .logo .logo__container {
   padding-left: 10px;
 }
</style>
