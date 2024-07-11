import java.io.BufferedReader
import java.io.InputStreamReader
import java.io.OutputStreamWriter

class ShellSessio1n {
    private val processBuilder = ProcessBuilder()
    private val process = processBuilder.command("bash").start()
    private val writer = OutputStreamWriter(process.outputStream)
    private val reader = BufferedReader(InputStreamReader(process.inputStream))
    private val errorReader = BufferedReader(InputStreamReader(process.errorStream))

    init {
        Runtime.getRuntime().addShutdownHook(Thread {
            writer.close()
            reader.close()
            errorReader.close()
            process.destroy()
        })
    }

    fun execute(command: String): String {
        writer.write("$command\n")
        writer.flush()

        val output = StringBuilder()
        val errorOutput = StringBuilder()

        // Read the output
        var line: String?
        while (true) {
            if (reader.ready()) {
                line = reader.readLine()
                if (line != null) {
                    output.append(line).append("\n")
                }
            } else {
                Thread.sleep(50)
                break
            }
        }

        // Read the error output
        while (true) {
            if (errorReader.ready()) {
                line = errorReader.readLine()
                if (line != null) {
                    errorOutput.append(line).append("\n")
                }
            } else {
                Thread.sleep(50)
                break
            }
        }

        return if (errorOutput.isNotEmpty()) {
            errorOutput.toString()
        } else {
            output.toString()
        }
    }
}

fun main() {
    val shellSession = ShellSession()

    println("Enter your commands. Type 'exit' to quit.")

    while (true) {
        print("> ")
        val command = readLine() ?: break

        if (command == "exit") {
            shellSession.execute("exit")
            break
        }

        val result = shellSession.execute(command)
        println(result)
    }
}
