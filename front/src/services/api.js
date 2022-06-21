import config from "@/config.js";
import { v4 as uuidv4 } from "uuid";


function getUserId() {
    const userJson = localStorage.getItem("auth");
    const user = JSON.parse(userJson);
    return user.id;
  }
  
// function getAccessToken() {
//     const jwtJson = localStorage.getItem("auth");
//     const jwt = JSON.parse(jwtJson);
//     return jwt.access_token;
//   }
  


export async function getTours(){
    const settings = {
        method: "GET",
        headers: {
            Authorization: "Bearer",
        },
    };
    const response = await fetch(`${config.API_PATH}/tours`, settings);
    const tours = await response.json();
    return tours;

}

export async function getTourDetail(tourId){
    const settings = {
        method: "GET",
        headers: {
            Authorization: "Bearer",
        },
    };
    const response = await fetch(`${config.API_PATH}/tours/${tourId}`, settings);
    return await response.json();
    
}
export async function deleteTour(tour){ 

    if (confirm("¿Está seguro de que quiere eliminar este tour?")) {
        await fetch(`${config.API_PATH}/tours/` + tour.tour_id, {
        method: "DELETE",
        headers: {
            Authorization: localStorage.userId,
            "Content-Type": "application/json",
        },
        });
    } else {
        return "";
    }
}

export async function addTour(tour){

    tour.tour_id = uuidv4();
    tour.favourite_tour = false;
    const settings = {
      method: "POST",
      body: JSON.stringify(tour),
      headers: {
        "Content-Type": "application/json",
        Authorization: getUserId(),
        
      },
    };
    
    await fetch(`${config.API_PATH}/tours`, settings);
    console.log(tour.tour_id)
  
  }

  export async function modifyTour(tour) {
    const settings = {
      method: "PUT",
      body: JSON.stringify(tour),
      headers: {
        "Content-Type": "application/json",
        Authorization: getUserId(),
      },
    };
    await fetch(`${config.API_PATH}/tours/${tour.tour_id}`, settings);
  }
  