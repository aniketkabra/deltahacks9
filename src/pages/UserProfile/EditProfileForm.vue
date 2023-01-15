<template>
  <card>
    <h4 slot="header" class="card-title">Patient: Victoria Justice</h4>
    <form>
      <div class="row">
        <div class="col-md-12">
          <base-input 
                type="email" 
                label="New Prescription"
                v-model="user.email"
                id="replaceText">
        </base-input>
        </div>
      </div>

      <!-- <div class="row">
        <div class="col-md-12">
          <div class="form-group">
            <label>New Prescription</label>
            <textarea rows="5"
                      class="form-control"
                      placeholder="Enter the new prescription here"
                      type="email"
                      id="replaceText">
            </textarea>
          </div>
        </div>
      </div> -->
      <div class="text-center">
        <button type="submit" class="btn btn-info btn-fill float-right" @click.prevent="updateProfile">
          Update Profile
        </button>
      </div>
      <div class="clearfix"></div>
    </form>
  </card>
</template>
<script>
  import Card from 'src/components/Cards/Card.vue'
  import abbr from './abbreviations.json'

  export default {
    components: {
      Card
    },
    data () {
      return {
        user: {
          company: 'Light dashboard',
          username: 'michael23',
          email: '',
          firstName: 'Mike',
          lastName: 'Andrew',
          address: 'Melbourne, Australia',
          city: 'melbourne',
          country: 'Australia',
          postalCode: '',
          aboutMe: `Lamborghini Mercy, Your chick she so thirsty, I'm in that two seat Lambo.`
        }
      }
    },
    methods: {
      updateProfile () {
        alert('Your data: ' + JSON.stringify(this.user))
      },
      makeLong(e) {
        if (String(`${e.code}`) === 'Space') {
          var temp = this.user.email.split(" ");
          console.log("TEMP IS : ", temp);
          var lastWord = temp.pop();
          console.log("last word IS : ", lastWord)
          if (lastWord.indexOf("\\") == 0) { // replaces any word starting with \ with abbreviation
            lastWord = abbr[lastWord.slice(1)];
            console.log("last word IS : ", lastWord)
            this.user.email = temp.join(" ") + ' ' + lastWord + ' ';
          }
          console.log("EMAIL IS: " , this.user.email);
        }
      }
    },
    mounted() {
      document.getElementById("replaceText").addEventListener("keyup", this.makeLong)
    }
  }

</script>
<style>

</style>
