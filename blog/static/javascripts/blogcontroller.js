class PostController{
    constructor(){
        this.title = document.getElementById("posts");
        this.addEvent();

    }
    addEvent(){
        this.title.addEventListener("mouseleave",()=>{
            alert("Volta Aqui!")
        });
    }
}