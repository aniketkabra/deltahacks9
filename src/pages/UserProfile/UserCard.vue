<template>
    <card class="card-user">
      <h4 slot="header" class="card-title">Upcoming appointments</h4>
      <div class="row">
        <div class="col-md-12">
            <b>January 5, 2023</b><br>
            9:30 am
        </div>
      </div>
    </card>
  </template>
  <script>
    import Card from 'src/components/Cards/Card.vue'
    export default {
      components: {
        Card
      },
      data () {
        return {
          details: [
            {
              title: '12',
              subTitle: 'Files'
            },
            {
              title: '2GB',
              subTitle: 'Used'
            },
            {
              title: '24,6$',
              subTitle: 'Spent'
            }
          ]
        }
      },
      methods: {
        getClasses (index) {
          var remainder = index % 3
          if (remainder === 0) {
            return 'col-md-3 col-md-offset-1'
          } else if (remainder === 2) {
            return 'col-md-4'
          } else {
            return 'col-md-3'
          }
        }
      }
    }
  
  </script>
  <style>
  
  </style>
  