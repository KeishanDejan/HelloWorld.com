program KKFC(input,output);
var x:array[1..10] of integer;
    y,i,j,temp:integer;

begin
    for y:=1 to 10 do
    begin
        writeln('Enter Number',y);
        read(x[y])
    end;
    
    
    for i:=10 downto 1 do
    begin
        for j:=1 to 10 do
        begin
            if (x[j] < x[j+1]) then
                temp:= x[j];
                x[j]:= x[j+1];
                x[j+1]:= temp;
        end;
    end;
    
    writeln(x[1]);
end.
