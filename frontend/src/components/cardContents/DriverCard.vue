
<template>
      <b-card
        
        :title="`${this.parsedData.first_name} ${this.parsedData.last_name}`"
        img-src="https://nwbus.com/wp-content/uploads/2020/11/Bus-Driver-Hiring-Tips-1200x800.jpg"
        img-alt="Image"
        img-top
        tag="article"
        style="max-width: 20rem;"
        class="mb-2"
        footer-tag="footer"
      >
        <b-card-text>
          Conductor Id: {{parsedData.driver_id}}
        </b-card-text>
        <b-card-text>
          Age: {{parsedData.age}}
        </b-card-text>
        <template #footer>
            <b-row align-h="between">
            <b-col cols="4">
              <b-button href="#" variant="primary">Edit</b-button>
            </b-col>
            <b-col cols="4">
              <b-button href="#" variant="danger">Delete</b-button>
            </b-col>
          </b-row>
        </template>
      </b-card>
</template>

<script>
    export default{
        props: ["parsedData", 'deleteFunction']
    }

</script>