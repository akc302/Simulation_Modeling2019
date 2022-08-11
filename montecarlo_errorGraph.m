function error=errorgraph()
    ax = -5
    bx = 5
    ay = -5
    by = 10
    t=2000
    r=5
    
    hold on;
    
    hits=0
    
    for i=1:t
        rand_x=rand() * (bx-ax) + ax;
        rand_y=rand() * (by-ay) + ay;
        func1 = 2*rand_x+10;
        func2 = -sqrt(r*r-rand_x.*rand_x)
        if rand_x*rand_y >0
            hits = hits+1;
            
        elseif func1>=rand_y && func2<=rand_y
            hits = hits+1;
            
        else
            
        end
        area = (hits/i)*150;
        err= abs(119-area);
        plot([i,i],[0,err]);
    end
    
    
    disp(area);