<template>
  <div class="content">
    <div class="container-fluid">
      <card>
      <div class="row">
        <div class="col-md-11">
          <h1>Welcome to your personal medical board. Here is your dashboard:</h1>
        </div>
      </div>
      <div class="row">
        <div class="col-xl-3 col-md-6">
          <h3>(insert images here)</h3>
        </div>
        <div class="col-xl-3 col-md-6">
          <h3>Your Patients</h3>
        </div>
      </div>
      <div class="row">
        <div class="col-md-12">
          <hr>
        </div>
      </div>


      <div class="row">
        <div class="col-md-6">
            <div class="row">
              <div class="col-md-6" style="min-width: 100%;">
                  <card>
                    <template slot="header">
                      <h3 class="title">Patients</h3>
                    </template>
                    <l-table :data="patientData.data"
                            :columns="patientData.columns">
                      <template slot="columns"></template>

                      <template slot-scope="{row}">
                        <td>{{row.title}}</td>
                        <td class="td-actions text-right">
                          <button 
                            type="button" class="btn-simple btn btn-xs btn-info" 
                            v-tooltip.top-center="editTooltip"
                            @click="$router.push(`/admin/patient/${row.title}`)"> View More
                            <i class="fa fa-arrow-up"></i>
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
                  <stats-card>
                    <div slot="header" class="icon-success">
                      <i class="nc-icon nc-chat-round text-success"></i>
                      <h2 class="card-title">Contact patient</h2>
                    </div>
                  </stats-card>
                </div>
            </div>
        </div>
        <div class="col-md-6">
          <card>
            <template slot="header">
              <h3 class="title">Schedule</h3>
            </template>
            <l-table :data="scheduleData.data"
                    :columns="scheduleData.columns">
              <template slot="columns"></template>

              <template slot-scope="{row}">
                <td>{{row.shiftid}}</td>
                <td>{{row.date}}</td>
                <td>{{row.time}}</td>
                <!-- <td class="td-actions text-right">
                  <button type="button" class="btn-simple btn btn-xs btn-info" v-tooltip.top-center="editTooltip">
                    <i class="fa fa-check"></i>
                  </button>
                </td> -->
              </template>
            </l-table>
            <div class="footer">
              <hr>
              <div class="stats">
                <i class="fa fa-history"></i> Updated 3 minutes ago
              </div>
            </div>
          </card>
                <br/>
                <br/>
                <br/>
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
    data () {
      return {
        editTooltip: 'See More',
        deleteTooltip: 'Remove',
        tableVar: [],
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
        patientData: {
          data: [
            {title: 'Isra Zahid', checked: false},
            {title: 'Tammy Zeng', checked: true},
            {
              title: 'Victoria Justice',
              checked: true
            },
            {title: 'Eddy Neufeld', checked: false},
            {title: 'Samia Anwar', checked: false},
            {title: 'Aniket Kabra', checked: false}
          ]
        },
        scheduleData: {
          data: [],
          columns: ['ShiftID', 'Date', 'Time']
        }
      }
    },
    methods: {
      async getShifts() {
        var myHeaders = new Headers();
        myHeaders.append("hypercare-scope", "eyJvcmdhbml6YXRpb25JZCI6NjA2LCJzdGF0dXMiOiJhZG1pbiJ9");
        myHeaders.append("Content-Type", "application/json");
        myHeaders.append("Authorization", "Bearer 656dd430d867f1a88ee35c82da1337afec2bca03")

        var graphql = JSON.stringify({
          query: "query FetchMyShifts($userId: ID!, $startDate: String!, $endDate: String, $limit: Int) {\n    admin {\n        user(id : $userId) {\n            shifts(startDate: $startDate, endDate: $endDate, limit: $limit) {\n                startDate\n                endDate\n                offset\n                shifts {\n                    ...ShiftFragment\n                }\n            }\n        }\n       \n    }\n}\n\nfragment ShiftFragment on Shift {\n    id\n    startDate\n    endDate\n    user {\n        id\n        username\n        firstname\n        lastname\n    }\n}",
          variables: {"userId":"f6442d7d-15ca-4e04-abca-8a0bc8463f51","startDate":"2023-01-02T06:03:38.610Z","endDate":"2023-12-03T06:03:38.610Z"}
        })
        var requestOptions = {
          method: 'POST',
          headers: myHeaders,
          body: graphql,
          redirect: 'follow'
        };

        let response = await fetch("https://api-prod.hypercare.com/graphql/private", requestOptions)
          .catch(error => console.log('error', error));
        const result = await response.json();
        var res = result.data.admin.user.shifts.shifts;

        var listOfTimes = [];
        Object.entries(res).forEach((entry) => {
          const [key, value] = entry;
          var date = new Date(value.startDate);
          date = date.toDateString();
          this.scheduleData.data.push({'shiftid': value.id, 'date': date, 'time': value.startDate.substr(12,4)})
          listOfTimes.push([value.id, date, value.startDate.substr(12,4)]);
        });

        console.log(this.scheduleData.data);
      }
    },
    mounted() {
      this.getShifts();
    }
  }
</script>
<style>

</style>
