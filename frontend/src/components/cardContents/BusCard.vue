
<template>
      <b-card
        :title="`${parsedData.plate}`"
        img-src="https://media.istockphoto.com/photos/white-passenger-bus-picture-id135327019?k=20&m=135327019&s=612x612&w=0&h=YJneXYFReSVuKSIFOy5wGIygeLeb1UquX4BWLk-MluI="
        img-alt="Image"
        img-top
        tag="article"
        style="max-width: 20rem;"
        class="mb-2"
        footer-tag="footer"
      >
        <b-card-text>
          Años de servicio: {{parsedData.years_of_service}}
        </b-card-text>
        <template #footer>
            <b-row align-h="between">
            <b-col cols="4">
              <b-button href="#" variant="primary">Edit</b-button>
            </b-col>
            <b-col cols="4">
              <b-button @click="deleteFunction" href="#" variant="danger">Delete</b-button>
            </b-col>
          </b-row>
        </template>
      </b-card>
</template>

<script>
    export default {
        props: ["parsedData", "deleteFunction"]

    };


</script>