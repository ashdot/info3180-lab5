<template>
  <div>
    <h2>Upload Form</h2>

     <form id="movieForm" @submit.prevent="saveMovie" enctype="multipart/form-data">
      
      <!-- Title -->
      <div class="form-group mb-3">
        <label for="title" class="form-label">Movie Title</label>
        <input 
          type="text" 
          name="title" 
          class="form-control"
          v-model="title"
        />
      </div>

      <!-- Description -->
      <div class="form-group mb-3">
        <label for="description" class="form-label">Description</label>
        <input 
          type="text" 
          name="description" 
          class="form-control"
          v-model="description"
        />
      </div>

      <!-- Poster -->
      <div class="form-group mb-3">
        <label for="poster" class="form-label">Poster</label>
        <input 
          type="file" 
          name="poster" 
          class="form-control"
          @change="handleFileUpload"
        />
      </div>

      <!-- Submit Button -->
      <button type="submit" class="btn btn-primary">
        Save Movie
      </button>



    </form>

    <p v-if="message">{{ message }}</p>

  </div>
</template>


<script setup>
import { ref , onMounted } from 'vue'


const title = ref('')
const description = ref('')
const poster = ref(null)
const message = ref('')

const csrfToken = ref("")


function getCsrfToken() {
  fetch('/api/v1/csrf-token')
    .then(response => response.json())
    .then(data => {
      console.log(data)
      csrfToken.value = data.csrf_token
    })
} 

onMounted(() => {
  getCsrfToken()
})

function handleFileUpload(event) {
  poster.value = event.target.files[0]
}

function saveMovie() {

  let movieForm = document.getElementById('movieForm')
  let form_data = new FormData(movieForm)

  fetch("/api/v1/movies", {
    method: "POST",
    body: form_data,
    headers: {
      "X-CSRFToken": csrfToken.value
    }
  })
  .then(response => response.json())
  .then(data => {
    console.log(data)

    message.value = "Movie uploaded successfully!"

    title.value = "" 
    description.value = "" 
    poster.value = null

  })
  .catch(error => {
    console.log(error)

    message.value = "Error uploading movie"
  })
}

</script>

<style>




</style>