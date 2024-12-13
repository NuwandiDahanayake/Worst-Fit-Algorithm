class MemoryBlock:
     
    def __init__(self, block_id, size):
        self.block_id = block_id
        self.size = size

    def __str__(self):
        return f"Block {self.block_id}: {self.size} units"


def worst_fit_allocate(memory_blocks, request_size):
     
    largest_idx = -1
    largest_size = -1

     
    for i, block in enumerate(memory_blocks):
        if block.size >= request_size and block.size > largest_size:
            largest_idx = i
            largest_size = block.size

     
    if largest_idx != -1:
        memory_blocks[largest_idx].size -= request_size
        print(f"Allocated {request_size} units from Block {memory_blocks[largest_idx].block_id}")

        
        if memory_blocks[largest_idx].size == 0:
            print(f"Block {memory_blocks[largest_idx].block_id} is now fully allocated and removed.")
            memory_blocks.pop(largest_idx)
        return True

    
    print(f"Request for {request_size} units could not be allocated.")
    return False


def display_memory_blocks(memory_blocks):
     
    if not memory_blocks:
        print("No available memory blocks.")
    else:
        print("Current Memory Blocks:")
        for block in memory_blocks:
            print(f"  {block}")


 
if __name__ == "__main__":
     
    memory_blocks = [
        MemoryBlock(1, 100),
        MemoryBlock(2, 150),
        MemoryBlock(3, 200),
        MemoryBlock(4, 30),
    ]

    print("Initial Memory Blocks:")
    display_memory_blocks(memory_blocks)
    print()

    
    requests = [150, 50, 300, 120, 400]

    for request in requests:
        print(f"Request: {request} units")
        worst_fit_allocate(memory_blocks, request)
        display_memory_blocks(memory_blocks)
        print("-")


 
    print("Final Memory Blocks:")
    display_memory_blocks(memory_blocks)
