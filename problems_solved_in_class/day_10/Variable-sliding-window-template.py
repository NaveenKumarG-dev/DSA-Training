
def sliding_window(arr,condition):
    left = 0
    window_state = {} # dict/Couunter/scalar -> depends on the problem
    result = 0

    for right in range(len(arr)):
        # EXPAND: add arr[right] to window state
        # eg. window_state[arr[right]] = window_state.get(arr[right],0) + 1

        # 2. SHRINK: while window is INVALID, remove from left
        while is_invalid(window_state,condition):
            #remove arr[left] from the window state
            left += 1
        # 3. UPDATE: window[left,right] is now valid

        result = max(result,right-left+1)

    return result