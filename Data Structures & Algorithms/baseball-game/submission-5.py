class Solution:
    def calPoints(self, operations: List[str]) -> int:
        def add(record):
            record.append(record[-1] + record[-2])
            return record
        
        def remove(record):
            record.pop()
            return record


        def multiple(record):
            record.append(record[-1] * 2)
            return record

        output_record = []

        for op in operations:
            if op == "+":
                add(output_record)
            elif op == "C":
                remove(output_record)
            elif op == "D":
                multiple(output_record)
            else:
                output_record.append(int(op))
            

        return sum(output_record)
