public class Libro {
    private String titulo;
    private String autor;
    private double precio;

    public Libro(String titulo, String autor, double precio) {
        this.titulo = titulo;
        this.autor = autor;
        this.precio = precio;
    }

    public String getTitulo() { return titulo; }
    public String getAutor()  { return autor; }
    public double getPrecio() { return precio; }

    
    public void mostrarInfo() {
        System.out.println("Título: " + titulo +
                           " | Autor: " + autor +
                           " | Precio: $" + precio);   

    }
}

// 
public class Main {
    public static void main(String[] args) {
        Libro[] biblioteca = new Libro[5]; 
        biblioteca[0] = new Libro("Cien años de soledad", "G. García Márquez", 50000);
        biblioteca[1] = new Libro("Don Quijote de la Mancha", "M. de Cervantes", 60000);
        biblioteca[2] = new Libro("La Odisea", "Homero", 45000);
        biblioteca[3] = new Libro("El Principito", "A. de Saint-Exupéry", 30000);
        libro[4] = new Libro("Rayuela", "Julio Cortázar", 55000);

        
        mostrarLibros(biblioteca);

        
        double total = calcularPrecioTotal(biblioteca);
        System.out.println("\nPrecio total de todos los libros: $" + total);
    }

    public static void mostrarLibros(Libro[] libros) {
        System.out.println("=== Información de los libros ===");
        for (int i = 0; i < libros.length; i++) {
            // libros[i] es un Libro: llamamos su método mostrarInfo()
            libros[i].mostrarInfo();
        }
    }

    // Suma los precios con un for clásico (sin filter/stream)
    public static double calcularPrecioTotal(Libro[] libros) {
        double acumulado = 0;
        for (int i = 0; i < libros.length; i++) {
            acumulado += libros[i].getPrecio();
        }
        return acumulado;
    }
}
