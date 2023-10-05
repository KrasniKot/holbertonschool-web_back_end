export default function guardrai(mathFunction) {
  const queue = [];

  try {
    const result = mathFunction();
    queue.push(result);
  } catch (error) {
    queue.push(error);
  } finally {
    queue.push('Guardrail was processed');
  }

  return queue;
}
