#include <GL/glut.h>

void display() {
    glClear(GL_COLOR_BUFFER_BIT);

    // Draw the house body
    glColor3f(0.0, 0.0, 0.5); // Dark blue color for the house
    glBegin(GL_POLYGON);
        glVertex2f(-0.5, -0.5);
        glVertex2f(0.5, -0.5);
        glVertex2f(0.5, 0.5);
        glVertex2f(-0.5, 0.5);
    glEnd();

    // Draw the roof
    glColor3f(0.0, 0.5, 0.0); // Green color for the roof
    glBegin(GL_TRIANGLES);
        glVertex2f(-0.6, 0.5);
        glVertex2f(0.0, 0.9);
        glVertex2f(0.6, 0.5);
    glEnd();

    // Draw the door
    glColor3f(1.0, 1.0, 0.0); // Yellow color for the door
    glBegin(GL_POLYGON);
        glVertex2f(-0.1, -0.5);
        glVertex2f(0.1, -0.5);
        glVertex2f(0.1, 0.4); 
        glVertex2f(-0.1, 0.4); 
    glEnd();

    // Draw the left window with red color
    glColor3f(1.0, 0.0, 0.0); // Red color for the window
    glBegin(GL_POLYGON);
        glVertex2f(-0.4, 0.0);
        glVertex2f(-0.2, 0.0);
        glVertex2f(-0.2, 0.2);
        glVertex2f(-0.4, 0.2);
    glEnd();

    // Draw the right window with red color
    glColor3f(1.0, 0.0, 0.0); // Red color for the window
    glBegin(GL_POLYGON);
        glVertex2f(0.2, 0.0);
        glVertex2f(0.4, 0.0);
        glVertex2f(0.4, 0.2);
        glVertex2f(0.2, 0.2);
    glEnd();

    // Draw the floor segment
    glColor3f(0.0, 0.0, 0.0); // Black color for the floor
    glBegin(GL_POLYGON);
        glVertex2f(-0.7, -0.7);
        glVertex2f(0.7, -0.7);
        glVertex2f(0.7, -0.5);
        glVertex2f(-0.7, -0.5);
    glEnd();

    glFlush();
}

void init() {
    glClearColor(1.0, 1.0, 1.0, 1.0); // White background
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0);
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(500, 500);
    glutInitWindowPosition(100, 100);
    glutCreateWindow("Ankon Karmokar (B190305039) Hut.");
    init();
    glutDisplayFunc(display);
    glutMainLoop();
    return 0;
}
