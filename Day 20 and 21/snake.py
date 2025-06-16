import turtle as t

# Constants
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)] 
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        """Initializes the snake by creating its body segments."""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]  # The leading segment of the snake

    def create_snake(self):
        """Creates the initial snake with three segments."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """
        Adds a new segment to the snake at the specified position.

        Args:
            position (tuple): (x, y) coordinates where the segment is placed.
        """
        new_segment = t.Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Adds a new segment to the tail of the snake."""
        self.add_segment(self.segments[-1].position())

    def move_snake(self):
        """
        Moves the snake forward by moving each segment to the position
        of the segment in front of it, and then moving the head forward.
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Turns the snake upward unless it's moving down."""
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        """Turns the snake downward unless it's moving up."""
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        """Turns the snake left unless it's moving right."""
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        """Turns the snake right unless it's moving left."""
        if self.head.heading() != 180:
            self.head.setheading(0)

    def wall_collision(self):
        """
        Checks if the snake's head has collided with the wall.

        Returns:
            bool: True if collision occurred, False otherwise.
        """
        if ((self.head.xcor() > 290 or self.head.xcor() < -290) or 
            (self.head.ycor() > 290 or self.head.ycor() < -290)):
            return True
        return False

    def tail_collision(self):
        """
        Checks if the snake's head has collided with its own body.

        Returns:
            bool: True if the head touches any segment of the tail.
        """
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False

    def reset(self):
        """Moves all snake segments off-screen and resets the snake."""
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
