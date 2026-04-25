def practice_2_custom_exceptions():
    """
    Practice creating and using custom exceptions
    """
    print("\n" + "="*50)
    print("EXERCISE 5: Custom Exceptions")
    print("="*50)
    
    # TODOo 1: Create custom exceptions
    class GameError(Exception):
        """Base class for game exceptions."""
        pass

    class InvalidMoveError(GameError):
        """Invalid game move."""
        
    # TODOo: Add __init__ with position and reason
        def __init__(self,position, reason):
            self.position = position
            self.reason = reason
            super().__init__(f"{position} & {reason}")

    class GameOverError(GameError):
        """Game has ended."""
        # TODOo: Add __init__ with winner
        def __init__(self,winner):
            self.winner = winner
            super().__init__(f"The winner is {winner}")
        
    
    # TODOo 2: Use custom exceptions
    class TicTacToe:
        def __init__(self):
            self.board = [[' ' for _ in range(3)] for _ in range(3)]
            self.current_player = 'X'
            self.game_over = False
        
        def make_move(self, row, col):
            # TODOo: Raise GameOverError if game_over is True
            if self.game_over:
                raise GameOverError("The game is over")
              
            
            # TODOo: Raise InvalidMoveError if position is out of bounds
            if row < 0 or row > 2 or col < 0 or col > 2:
                raise InvalidMoveError((row,col), "Out of bounds")
            
            
            # TODOo: Raise InvalidMoveError if position is taken
            if self.board[row][col] != ' ':
                raise InvalidMoveError((row, col), "The position is taken")
           
            self.board[row][col] = self.current_player
# Test the game
    game = TicTacToe()

    test_moves = [
    (0, 0), # Valid
    (0, 0), # Already taken
    (5, 5), # Out of bounds
    ]
    
    for row, col in test_moves:
        try:
            game.make_move(row, col)
            print(f"✅ Move ({row}, {col}) successful")
        except InvalidMoveError as e:
            print(f"Invalid move: {e}")
        except GameOverError as e:
            print(f"🏁 Game over: {e}")
            
practice_2_custom_exceptions()


print("\n")

def practice_3_complete_system():
    """
    Build a complete error handling system
    """
    
    print("\n" + "="*50)
    print("EXERCISE 6: Complete Error Handler")
    print("="*50)
    
# TODOo: Build a file processing system with proper error handling
    class FileProcessor:
        def __init__(self):
            self.processed_files = []
            self.failed_files = []
            
        def process_file(self, filename):
            """
            Process a single file with complete error handling.
            """
            # TODO: Implement with try-except-else-finally
            file = None
            try:
                file = open(filename, 'r')
                
            except FileNotFoundError as e:
                print(f"File not found: {filename}")
                self.failed_files.append(filename)
                
            except PermissionError as e:
                print(f"Permission not allowed for: {filename}")
                self.failed_files.append(filename)
                
            except Exception as e:
                print(f"Error: {filename}: {e}")
                self.failed_files.append(filename)
            else:
                content = file.read()
                self.processed_files.append(filename)
            
            finally:
                
                if file:
                    file.close()
            # TODO: Handle FileNotFoundError
            # TODO: Handle PermissionError
            # TODO: Handle general exceptions
            # TODO: Ensure file is closed
            
            
        def process_directory(self, directory):
            """
            Process all files in directory, collecting errors.
            """
        # TODO: Process each file
            for filename in directory:
                self.process_file(filename)
            
        # TODO: Continue on errors
        # TODO: Track successes and failures
        
    
        def get_report(self):
            """
            Get processing report.
            """
            return {
        "processed_files": self.processed_files,
        "failed_files": self.failed_files
    }
# TODO: Return summary of processing
            
        
# Test the processor
    processor = FileProcessor()
    
    test_files = [
        "valid.txt",
        "missing.txt",
        "/root/restricted.txt"
]
    for filename in test_files:
        processor.process_file(filename)
        
    report = processor.get_report()
    print(f"Report: {report}")
     
# Run the practice
practice_3_complete_system()