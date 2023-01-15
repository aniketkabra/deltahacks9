<template>
    <div class="content">
      <div class="container-fluid">
        <card>
        <div class="row">
          <div class="col-md-6">
            <button @click="$router.push('/admin/')">&lt;- Back</button>
            <h1>Patient: {{ this.patientName }}</h1>
          </div>
        </div>
        <div class="row">
          <div class="col-md-12">
            <hr>
          </div>
        </div>

        <div class="row">
            <div class="col-md-4">
                <card>
                    <template slot="header">
                    <h3 class="title">Current Prescriptions</h3>
                    </template>
                    <l-table :data="prescriptionData.data"
                            :columns="prescriptionData.columns">
                    <template slot="columns"></template>

                    <template slot-scope="{row}">
                        <td>{{row.title}}</td>
                        <td class="td-actions text-right">
                        <button type="button" class="btn-simple btn btn-xs btn-info" 
                            data-toggle="collapse" data-target="#collapseInfo"
                            aria-expanded="false" aria-controls="collapseInfo">
                            <i class="fa fa-arrow-down"></i>
                        </button>
                        <div class="collapse" id="collapseInfo">
                            <card>
                                Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea proident.
                            </card>
                        </div>
                        </td>
                    </template>
                    </l-table>
                    <div class="footer">
                        <button @click="$router.push(`/admin/add/prescription/${patientName}`)">+ Add new prescription</button>
                        <hr>
                    </div>
                </card>
            </div>
            <div class="col-md-8">
                <div class="row">
                    <div class="col-md-6" style="min-width: 100%;">
                        <card>
                            <template slot="header">
                                <h3 class="title">Upcoming Appointments</h3>
                            </template>
                            <l-table :data="appointmentData.data"
                                    :columns="appointmentData.columns">
                                <template slot="columns"></template>
                
                                <template slot-scope="{row}">
                                <td>{{row.title}}</td>
                                <td class="td-actions text-right">
                                    <button type="button" class="btn-simple btn btn-xs btn-info" v-tooltip.top-center="editTooltip">
                                    <i class="fa fa-check"></i>
                                    </button>
                                </td>
                                </template>
                            </l-table>
                            <div class="footer">
                                <hr>
                                <div class="stats">
                                <i class="fa fa-history"></i> Updated 3 minutes ago
                                </div>
                            </div>
                        </card>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6" style="min-width: 100%;">
                        <card>
                            <template slot="header">
                                <h3 class="title">Notes</h3>
                            </template>
                            <l-table :data="notesData.data"
                                    :columns="notesData.columns">
                                <template slot="columns"></template>
                
                                <template slot-scope="{row}">
                                <td>{{row.title}}</td>
                                <td class="td-actions text-right">
                                    <button type="button" class="btn-simple btn btn-xs btn-info" v-tooltip.top-center="editTooltip">
                                    <i class="fa fa-check"></i>
                                    </button>
                                </td>
                                </template>
                            </l-table>
                            <div class="footer">
                                <hr>
                            </div>
                        </card>
                    </div>
                </div>
            </div>
        </div>
        </card>
      </div>
    </div>
  </template>
  
  <script>
    import ChartCard from 'src/components/Cards/ChartCard.vue'
    import StatsCard from 'src/components/Cards/StatsCard.vue'
    import LTable from 'src/components/Table.vue'
  
    export default {
      components: {
        LTable,
        ChartCard,
        StatsCard
      },
      props: {
        "patientName": String
      },
      data () {
        return {
          editTooltip: 'See More',
          deleteTooltip: 'Remove',
          pieChart: {
            data: {
              labels: ['40%', '20%', '40%'],
              series: [40, 20, 40]
            }
          },
          lineChart: {
            data: {
              labels: ['9:00AM', '12:00AM', '3:00PM', '6:00PM', '9:00PM', '12:00PM', '3:00AM', '6:00AM'],
              series: [
                [287, 385, 490, 492, 554, 586, 698, 695],
                [67, 152, 143, 240, 287, 335, 435, 437],
                [23, 113, 67, 108, 190, 239, 307, 308]
              ]
            },
            options: {
              low: 0,
              high: 800,
              showArea: false,
              height: '245px',
              axisX: {
                showGrid: false
              },
              lineSmooth: true,
              showLine: true,
              showPoint: true,
              fullWidth: true,
              chartPadding: {
                right: 50
              }
            },
            responsiveOptions: [
              ['screen and (max-width: 640px)', {
                axisX: {
                  labelInterpolationFnc (value) {
                    return value[0]
                  }
                }
              }]
            ]
          },
          barChart: {
            data: {
              labels: ['Jan', 'Feb', 'Mar', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
              series: [
                [542, 443, 320, 780, 553, 453, 326, 434, 568, 610, 756, 895],
                [412, 243, 280, 580, 453, 353, 300, 364, 368, 410, 636, 695]
              ]
            },
            options: {
              seriesBarDistance: 10,
              axisX: {
                showGrid: false
              },
              height: '245px'
            },
            responsiveOptions: [
              ['screen and (max-width: 640px)', {
                seriesBarDistance: 5,
                axisX: {
                  labelInterpolationFnc (value) {
                    return value[0]
                  }
                }
              }]
            ]
          },
          prescriptionData: {
            data: [
              {title: 'Cyclosporine', checked: false},
              {title: 'Tacrolimus', checked: true},
              {
                title: 'Imuran',
                checked: true
              },
            ]
          },
          appointmentData: {
            data: [
              {title: 'January 29, 2023: 9:30 AM, Room AB2', checked: false},
            ]
          },
          notesData: {
            data: [
              {title: 'Experienced mild fatigue and stomach aches after increasing cyclosporine.', checked: false},
            ]
          }
        }
      },
      methods: {
        async someFunc() {
  
        }
      }
    }
  </script>
  <style>
  
  </style>
  