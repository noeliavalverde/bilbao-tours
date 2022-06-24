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


export async function getTourStops(){
  const settings = {
      method: "GET",
      headers: {
          Authorization: "Bearer",
      },
  };
  const response = await fetch(`${config.API_PATH}/tour-stops`, settings);
  const tour_stops = await response.json();
  return tour_stops;

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
            Authorization: getUserId(),
            
        },
        });
    } else {
        return "";
    }
}
export async function deleteStop(stop){ 

  if (confirm("¿Está seguro de que quiere eliminar esta visita?")) {
      await fetch(`${config.API_PATH}/tour-stops/` + stop.stop_id, {
      method: "DELETE",
      headers: {
          Authorization: getUserId(),
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
    
  
  }
  export async function addStop(stop){

    stop.stop_id = uuidv4();
   
    const settings = {
      method: "POST",
      body: JSON.stringify(stop),
      headers: {
        "Content-Type": "application/json",
        Authorization: getUserId(),
        
      },
    };
    
    await fetch(`${config.API_PATH}/tour-stops`, settings);
    
  
  }

  export async function addTourStops(tour_id, stops){
     
    const settings = {
      method: "POST",
      body: JSON.stringify({"tour_id":tour_id, "stops": stops}),
      
      headers: {
        "Content-Type": "application/json",
        Authorization: getUserId(),
      },
    };
   
    await fetch(`${config.API_PATH}/add-stops/${tour_id}`, settings);
    
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
  