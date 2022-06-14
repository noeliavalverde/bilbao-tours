import config from "@/config.js";
import { v4 as uuidv4 } from "uuid";

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
        
      },
    };
    await fetch(`${config.API_PATH}/tours`, settings);
  }
  