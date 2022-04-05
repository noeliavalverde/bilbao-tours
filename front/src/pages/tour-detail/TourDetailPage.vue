<template>
  <div class="tour-detail-page">

  <h2>Nombre ruta: {{tour.tour_name}}</h2>
  <h3>Descripción ruta: {{tour.tour_description}}</h3>
  <ul v-for="filter in tour.filters" :key="filter">
    <li>filtros: {{filter}}</li>
  </ul>
  <p>barrio: {{tour.quarter}}</p>

  <section v-for="stop in tour.tour_stops" :key="stop.stop_id" class="stop-wrapper">

    
    <h4>{{stop.stop_name}}</h4>
    <p>{{stop.stop_description}}</p>
    <figure class="image-wrapper"><img :src="stop.before_picture" :alt="stop.before_alt_text">
    <figcaption>{{stop.before_figcaption}}</figcaption>
    </figure>
    <figure class="image-wrapper"><img :src="stop.after_picture" :alt="stop.after_alt_text">
    <figcaption>{{stop.after_figcaption}}</figcaption>
    </figure>
  </section>

  </div>

  <pre>{{$data}}</pre>
</template>

<script>

export default {
  name: 'TourDetailPage',
  data() {
    return {
        tour: {},
        
    }
  },
  mounted() {
    this.loadData()
    
  },
  methods: {
     loadData(){
       this.tour = {
       tour_name:"Ruta 1",
       tour_id:"tour001",
       tour_description:"Breve explicacion ruta 1",
       favorite_tour:true,
       completed:false,
       filters:["arquitecture", "industrial"],
       quarter:["abando", "casco", "deusto", "uribarri"],
       tour_stops:[{"stop_id": "stop001",
                         "stop_name":"Plaza Circular",
                         "stop_description":"Don Diego López de Haro, Señor de Bizkaia, funda la villa en 1300, y aún la vigila desde lo alto de su monolito en la Plaza Circular rodeado del centro de negocios de esta pujante ciudad. Los tilos dan sombra y perfume a la Gran Vía invitándonos a pasear, a mirar tiendas y a admirar fachadas.",
                         "before_picture":"https://i.pinimg.com/736x/a0/c6/57/a0c657021b83d2edd1c7c26d59c695a9--basque-country-bilbao.jpg",
                         "before_figcaption":"Plaza circular - antes",
                         "before_alt_text":"Plaza circular",
                         "after_picture":"https://abraseguridad.es/wp-content/uploads/2017/12/Edificio-Plaza-Circular.jpg",
                         "after_figcaption":"Plaza circular - actual",
                         "after_alt_text":"Plaza circular",
                         },
                    {"stop_id": "stop002",
                     "stop_name":"Alameda Urquijo/Bertendona",
                     "stop_description":"Las sedes del Banco de España y del BBVA nos conducen hacia la Alameda Urquijo y a la Residencia, iglesia neogótica de piedra y ladrillo de los Jesuitas, entre fachadas eclécticas y miradores. Continuamos por Urquijo hasta encontrar a nuestra izquierda Bertendona. En esta calle descubrimos el Teatro Campos que parece tener vergüenza de ser diferente, de ser modernista. Contrasta con la rotunda monumentalidad de su vecino, el edificio de Correos, ejemplo de la arquitectura franquista, que sin complejos mira hacia Urquijo.",
                     "before_picture":"https://scontent.fbio1-1.fna.fbcdn.net/v/t1.18169-9/970471_412930742161727_1705928822_n.jpg?_nc_cat=108&ccb=1-5&_nc_sid=9267fe&_nc_ohc=7Gg1qcGm7c4AX-5nFlS&_nc_ht=scontent.fbio1-1.fna&oh=00_AT-0-6rhE19UyW-tQj750z4aVj3HrIvjVPbUaesbC7vn7Q&oe=626B72EC",
                     "before_figcaption":"Alameda Urquijo - antes",
                     "before_alt_text":"Alameda Urquijo",
                     "after_picture":"https://bilbaoarquitecturayurbanismo2ohome.files.wordpress.com/2019/11/p1080368.jpg",
                     "after_figcaption":"Alameda Urquijo - actual",
                     "after_alt_text":"Alameda Urquijo",
                     },
                     {"stop_id": "stop002",
                     "stop_name":"Teatro Campos Elíseos",
                     "stop_description":"El Teatro Campos Elíseos forma parte de la vida de Bilbao desde 1902, cuando se inauguró en lo que aquel entonces era el solar de los ‘Jardines de los Campos Elíseos’. Obra del arquitecto Alfredo Acebal y el decorador francés Jean Batiste Darroguy (quien diseñó su característica fachada), el edificio modernista está hoy catalagado como Bien de Interés Cultural. En plena expansión económica, urbanística y cultural de Bilbao, pronto el teatro, conocido ya como ‘la bombonera de Bertendona’, se convirtió en una de las salas de mayor categoría artística, y en la plataforma escénica que impulsó con mayor acierto la pujante ópera vasca, – por aquel entonces recién concebida. Además, cultivaba la programación dramática, cómica, y de cine, una función a la que terminó por dedicarse en exclusividad. Sin embargo, diversos infortunios, como el atentado que sufrió en 1978 llevaron al Teatro Campos Elíseos a su deterioro y al cese de su actividad. En 2010, un minucioso trabajo de rehabilitación consiguió recuperar en la medida de lo posible el diseño original modernista, a la vez que incrementó espacios y volúmenes. Actualmente la superficie del edificio es de 7300m2, donde conviven dos salas de representación y un centro de formación artístico y tecnológico. La modernización de sus instalaciones incluye además las soluciones tecnológicas más avanzadas para la representación de las artes escénicas. Desde 2017 el teatro está gestionado por Klemark Espectáculos Teatrales con un objetivo claro: devolver a la ciudad de Bilbao la riqueza artística y cultural que ha caracterizado durante años al Teatro Campos Elíseos. Un lugar donde las compañías nacionales e internacionales se den la mano con los artistas vascos, atendiendo siempre a la máxima calidad de sus espectáculos.",
                     "before_picture":"https://i.pinimg.com/originals/3a/26/ce/3a26cef27dcea9e511b1ce2533b94529.jpg",
                     "before_figcaption":"Teatro Campos Elíseos - antes",
                     "before_alt_text":"Teatro Campos Elíseos",
                     "after_picture":"https://images.adsttc.com/media/images/5128/a0e8/b3fc/4b11/a700/4a97/large_jpg/1284057850-mg-0006modb.jpg?1414370082",
                     "after_figcaption":"Teatro Campos Elíseos - actual",
                     "after_alt_text":"Teatro Campos Elíseos",
                     },
                ]
          
       
    }
     },

  },
}
</script>

<style scoped>

.stop-wrapper{
  margin-bottom: 2em;
}

</style>